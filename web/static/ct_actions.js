async function ctFetch(url, method='POST', body={}) {
  const r = await fetch(url, {
    method,
    headers: {'Content-Type':'application/json'},
    body: method==='GET' ? undefined : JSON.stringify(body)
  });
  if (!r.ok) {
    let txt = await r.text().catch(()=> '');
    throw new Error('HTTP '+r.status+' '+txt);
  }
  return r.json();
}

async function ctEdit(rid) {
  const fields = ['player','set','year','number','sport','market_value','purchase_price','grade'];
  const payload = { row_id: String(rid), updates: {} };
  for (const f of fields) {
    const v = prompt(`Set ${f} (leave blank to skip)`);
    if (v !== null && v !== '') payload.updates[f] = v;
  }
  if (!Object.keys(payload.updates).length) return;
  try {
    await ctFetch('/api/card/update','PATCH',payload);
    alert('Updated. Reloading…'); location.reload();
  } catch(e) { alert('Edit failed: '+e.message); }
}

async function ctDelete(rid) {
  if (!confirm('Delete this card from active CSV?')) return;
  try {
    await ctFetch('/api/card/delete','POST',{ row_id: String(rid) });
    alert('Deleted. Reloading…'); location.reload();
  } catch(e) { alert('Delete failed: '+e.message); }
}

async function ctDelImg(rid, side) {
  if (!['front','back'].includes(side)) return;
  if (!confirm(`Delete ${side} image from disk & clear field?`)) return;
  try {
    await ctFetch('/api/card/delete_image','POST',{ row_id:String(rid), side });
    alert('Image cleared. Reloading…'); location.reload();
  } catch(e) { alert('Delete-image failed: '+e.message); }
}
