from pathlib import Path

VAULT_ROOT = Path('.')

changed = []
removed_blocks = 0

for p in VAULT_ROOT.rglob('*.md'):
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not text.startswith('---'):
        continue
    parts = text.split('---', 2)
    if len(parts) < 3:
        continue

    fm_lines = parts[1].splitlines(True)  # keep newlines
    body = parts[2]

    out = []
    i = 0
    removed_here = 0

    while i < len(fm_lines):
        line = fm_lines[i]
        if line.startswith('annotation-target:'):
            removed_here += 1
            i += 1
            # If annotation-target had a YAML block (unlikely), skip indented continuation lines.
            while i < len(fm_lines) and fm_lines[i].startswith('  '):
                # stop if we somehow hit a new top-level key
                if fm_lines[i].lstrip() == fm_lines[i] and ':' in fm_lines[i]:
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
            removed_blocks += removed_here

print(f"files_changed={len(changed)}")
print(f"annotation_target_keys_removed={removed_blocks}")
for fp in changed[:50]:
    print(fp)
if len(changed) > 50:
    print(f"... and {len(changed)-50} more")
