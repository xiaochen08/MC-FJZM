# Windows UTF-8 red gate

## Critical rule

`severity: red`. Run this gate before any Mod source, model, GUI, texture, animation, or localized resource is created. Encoding failures are root-cause failures: fixing visible mojibake later does not repair already-corrupted source, JSON, language files, generated resources, logs, or hashes.

Fail closed. Do not continue because “the console looks fine,” because Java 18+ usually defaults to UTF-8, or because one file opened correctly. Save evidence in `encoding-preflight.json` and validate it with:

```powershell
python -X utf8 scripts/validate_encoding_preflight.py encoding-preflight.json --required-phase host
python -X utf8 scripts/validate_encoding_preflight.py encoding-preflight.json --required-phase project
```

## Phase A: host gate before the Mod shell

Only the approved unified project root and a disposable sentinel area may exist at this stage.

1. Require PowerShell 7. Set console input and output to UTF-8 for the current process; do not change the system locale, registry, global code page, or global PATH.
2. Use explicit UTF-8 without BOM for every generated text file. Use LF line endings. Never rely on Windows ANSI, GBK, the active code page, or an API's implicit default.
3. Write and read a Chinese sentinel such as `方界造模-中文编码-✓-é-Ω` using explicit UTF-8. Compare exact Unicode text and SHA-256 bytes.
4. Run a strict UTF-8 decode scan over every existing project text file in scope. Reject invalid byte sequences, unexpected UTF-8 BOM files, replacement characters, and mixed encodings.
5. Inventory installed JDKs and inspect `file.encoding`, `native.encoding`, console input and output, but do not edit global Java settings.

Record `status: host_passed` only when PowerShell, console input and output, UTF-8 without BOM writes, LF line endings, the Chinese sentinel, and the strict UTF-8 decode scan all pass.

## Phase B: project gate after the official empty shell

The host gate authorizes only the official empty loader/template shell. All custom project files remain blocked until `status: project_passed`.

1. Add `.editorconfig` with `charset = utf-8`, `end_of_line = lf`, and final-newline rules; add a scoped `.gitattributes` policy for stable LF text without rewriting unrelated files.
2. Set the Gradle daemon JVM explicitly with `-Dfile.encoding=UTF-8` in project-local configuration. Do not use a global environment variable as the primary fix.
3. Configure every `JavaCompile` task with explicit UTF-8 source encoding. Configure resource filtering/copy tasks explicitly when they read text.
4. Run the project-local `gradlew.bat` diagnostics and capture the actual Gradle daemon JVM and encoding.
5. Add a disposable localized Java/resource sentinel, build it, read it through the same runtime path that will load language/GUI/resource files, then remove only the known sentinel after recording its hashes.
6. Re-run the strict UTF-8 decode scan and the localized build. Reject console mojibake, JSON/resource parse failures, replacement characters, BOM violations, or byte drift.

Only `project_passed` authorizes custom Java, JSON, language, GUI, model metadata, texture metadata, animation, audio, or particle resources.

## Required report fields

```json
{
  "schema_version": 1,
  "severity": "red",
  "status": "host_passed | project_passed",
  "host_checks": {
    "powershell7": "passed",
    "console_input_encoding": "utf-8",
    "console_output_encoding": "utf-8",
    "default_text_write": "utf-8-no-bom",
    "line_endings": "lf",
    "chinese_sentinel_round_trip": "passed",
    "strict_utf8_decode_scan": "passed",
    "bom_violations": 0,
    "invalid_utf8_files": 0
  },
  "project_checks": {
    "java_process_file_encoding": "utf-8",
    "gradle_daemon_file_encoding": "utf-8",
    "java_compile_encoding": "utf-8",
    "localized_resource_round_trip": "passed",
    "localized_build": "passed",
    "strict_utf8_decode_scan": "passed"
  }
}
```

JDK 18 and later standardize UTF-8 for many default Java APIs, but console I/O and older/mixed toolchains still require explicit evidence. Verify current behavior from primary sources at execution time: OpenJDK JEP 400 (https://openjdk.org/jeps/400), the exact JDK documentation, the exact Gradle compatibility matrix, and the exact loader/plugin documentation.
