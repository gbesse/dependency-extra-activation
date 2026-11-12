from collections import deque
from .common import identifier,unique_ids
def run(data):
 packages=data['packages'];roots=data['roots']
 if len(packages)>1000 or len(roots)>1000:raise ValueError('size')
 unique_ids(packages);index={p['id']:p for p in packages};active={};queue=deque();processed={};reasons=[]
 def activate(name,extras,parent):
  identifier(name)
  if name not in index:raise ValueError('missing_package_metadata')
  if not isinstance(extras,list)or len(extras)>100:raise ValueError('extras')
  for e in extras:identifier(e)
  first=name not in active;old=active.setdefault(name,set());before=len(old);old.update(extras)
  if first or len(old)!=before:queue.append(name);reasons.append({'package':name,'from':parent,'activated_extras':sorted(extras)})
 for r in roots:activate(r['package'],r.get('extras',[]),None)
 while queue:
  name=queue.popleft();signature=frozenset(active[name])
  if processed.get(name)==signature:continue
  processed[name]=signature
  requirements=index[name].get('requirements',[])
  if len(requirements)>100:raise ValueError('requirements')
  for req in requirements:
   when=req.get('when_extra')
   if when is None or identifier(when)in active[name]:activate(req['package'],req.get('activate_extras',[]),name)
 return {'closure':[{'package':p,'extras':sorted(active[p])}for p in sorted(active)],'activation_reasons':reasons,'pep508_text_parsed':False,'versions_resolved':False}
