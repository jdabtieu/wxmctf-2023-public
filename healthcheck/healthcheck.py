from datetime import datetime
import subprocess
import time
import traceback
import json

from getinstance import getinstance, requests

def run(outfile):
  passed = []
  disabled = []
  with open("config.json", "r") as f:
    data = json.load(f)

  for name, conf in data["challs"].items():
    if conf.get("disabled"):
        disabled.append(name)
        continue
    try:
        with open(f"{name}.flag", "r") as flagfile:
            flag = flagfile.readline().strip()
    except FileNotFoundError:
        outfile.write(f"**{name} failed due to: bad configuration**\n")
        continue
    time.sleep(3)
    if conf.get("instancer", False):
        try:
            host, port = getinstance(data["instancer"]["session"], data["instancer"]["host"], conf["slug"])
        except LookupError:
            outfile.write(f"**{name} failed due to: failed to get instance (non-200)**\n")
            continue
        except KeyError:
            outfile.write(f"**{name} failed due to: failed to get instance (bad JSON)**\n")
            continue
        except requests.Timeout:
            outfile.write(f"**{name} failed due to: failed to get instance (timed out)**\n")
            continue
        except Exception:
            outfile.write(f"**{name} failed due to: failed to get instance**\n")
            continue
    else:
        host = conf.get("host")
        port = conf.get("port")
    passes = 0
    runs = 3
    timed_out = False
    crashed = False
    for i in range(runs):
        try:
          r = subprocess.run(["python3", f"{name}.py", host, str(port)], capture_output=True, timeout=15)
          if r.returncode != 0 and flag.encode('utf-8') not in r.stdout:
            crashed = True
          elif flag.encode('utf-8') in r.stdout:
            passes += 1
            runs = i + 1
            break
          else:
            pass  # Generic fail
        except subprocess.TimeoutExpired:
            timed_out = True

    if passes > 0:
        passed.append(f"{name} ({passes}/{runs})")
    elif crashed:
        outfile.write(f"**{name} failed due to: exploit crashed and failed**\n")
    elif timed_out:
        outfile.write(f"**{name} failed due to: exploit timed out**\n")
    else:
        outfile.write(f"**{name} failed due to: exploit failed**\n")

  outfile.write("Passed: " + ", ".join(passed) + "\n")
  outfile.write("Disabled: " + ", ".join(disabled) + "\n")
  if len(passed) + len(disabled) == len(data["challs"]):
    outfile.write(f"All challenges passed\n")

def main():
  outfile = open("result.txt", "w")
  s = datetime.now()
  outfile.write(f"Starting healthcheck at {s}\n")
  try:
    run(outfile)
  except Exception:
    outfile.write("**Healthcheck raised an exception:**\n")
    outfile.write(traceback.format_exc())
  outfile.write(f"Healthcheck completed in {datetime.now() - s}\n")
  with open("config.json", "r") as f:
    outfile.write("```json\n")
    outfile.write(json.dumps(json.load(f)["challs"]).replace("},", "},\n").replace(" ", ""))
    outfile.write("```")
  outfile.close()

if __name__ == "__main__":
  main()
