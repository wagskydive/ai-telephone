# Initiative-Based Outbound Calls

The helper `src.outbound.run_outbound` selects personalities whose `initiative` value exceeds a random threshold. For each selected character the provided `originate` function is called with the personality's extension.

Example usage:
```python
from src.outbound import run_outbound
from src.personalities import load_personalities

personalities = load_personalities(Path('data/personalities.json'))
run_outbound(personalities, originate=lambda ext: print(f'call {ext}'))
```
