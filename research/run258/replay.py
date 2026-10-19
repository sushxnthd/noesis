"""Run258: exact certificate replay against the immutable archive."""
import os,runpy
for seed in (16003,16005,16006,16007,16008):
 for checker in ("check_descendant","independent_descendant"):
  os.environ["NOESIS_PARAMS"]=f"research/run256/descendant_{seed}.json"
  os.environ["NOESIS_CERT_PATH"]=f"research/run257/CERTIFICATE_{seed}.json"
  runpy.run_path(f"research/run256/{checker}.py",run_name="__main__")
print("RUN258 exact replay: 5/5 x 2 checkers PASS")
