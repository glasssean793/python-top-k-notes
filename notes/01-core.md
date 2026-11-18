# Find the largest k values: implementation

## What the example does

heapq.nlargest is useful when k is small relative to the input. Duplicates are retained; negative k is rejected as an invalid request.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
{
  "items": [
    5,
    1,
    8,
    8,
    3
  ],
  "k": 3
}
```

Expected result:

```json
[
  8,
  8,
  5
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
