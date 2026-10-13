import json
from datetime import datetime, timezone

def write_log(path, level, event, **fields):
    record={"timestamp":datetime.now(timezone.utc).isoformat(),"level":level,"event":event,**fields}
    with open(path,"a",encoding="utf-8") as f:
        f.write(json.dumps(record)+"\n")
    return record