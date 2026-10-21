import sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research/kernel001/run311'
sys.path.insert(0,str(P))
import search311, independent311
def test_run311_reproduction():
    search311.main()
    independent311.main()
