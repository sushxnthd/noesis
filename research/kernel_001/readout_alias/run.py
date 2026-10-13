from core import F, H, M, train, failure
import json

if __name__ == '__main__':
    print(json.dumps({'shortcut':train(F(-1,4),F(3,4))[0], 'algorithm':train(F(3,4),F(-1,4))[0]}, indent=2))
