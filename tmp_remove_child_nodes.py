from pathlib import Path

VAULT_ROOT = Path('.')

changed = []
repl_files = 0
removed_blocks = 0

for p in VAULT_ROOT.rglob('*.md'):
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---'):
        continue

    parts = text.split('---', 2)
    if len(parts) < 3:
        continue

    fm = parts[1].splitlines(True)  # keep newlines
    body = parts[2]

    out = []
    i = 0
    removed_here = 0
    while i < len(fm):
        line = fm[i]
        # match key exactly at beginning of line
        if line.startswith('child nodes:'):
            removed_here += 1
            # skip this line
            i += 1
            # skip any YAML block/list entries that are indented (common pattern: two spaces + '-')
            while i < len(fm) and (fm[i].startswith('  -') or fm[i].startswith('    -') or fm[i].startswith('  ')):
                # Only skip continuation lines until we hit a new top-level key (non-indented)
                # If the line is blank, it's fine to skip as part of the block.
                # But if it's an indented continuation for some other key, this would be unsafe.
                # So: stop skipping when we see something that looks like another key at top-level.
                if fm[i].lstrip() == fm[i] and ':' in fm[i]:
                    break
                i += 1
            continue
        out.append(line)
        i += 1

    if removed_here:
        new_text = '---' + ''.join(out) + '---' + body
        if new_text != text:
            p.write_text(new_text, encoding='utf-8')
            changed.append(str(p))
            repl_files += 1
            removed_blocks += removed_here

print(f"files_changed={repl_files}")
print(f"child_nodes_blocks_removed={removed_blocks}")
for fp in changed[:50]:
    print(fp)
if len(changed) > 50:
    print(f"... and {len(changed)-50} more")
