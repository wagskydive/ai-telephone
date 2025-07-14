# Name Recognition Persistence

During each call the system attempts to infer the caller's name from the
conversation using simple regex patterns. Detected names are stored in
`memory/names.json` keyed by the caller's extension. The next time the same
caller interacts with any personality, the stored name is included in the
prompt so the AI can greet them personally.

Names are saved via `memory_logger.remember_name` whenever
`log_interaction` writes a new entry.
