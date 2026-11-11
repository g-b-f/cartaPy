# Changelog

All notable changes to this project are documented in this file

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [2.1.5] - 2026-11-11

### Changed

- Rename the Rust wrapper module to avoid collisions
- Set the new `disable_native` conversion option to `false` by default
- Fix Python 3.9 compatibility issues caused by newer annotation syntax

## [2.1.4] - 2026-10-31

### Changed

- Update the underlying `carta` crate to 0.0.13

## [2.1.3] - 2026-10-18

### Changed

- Update CI

## [2.1.2] - 2026-10-17

### Changed

- Update CI

## [2.1.1] - 2026-10-17

### Changed

- Update CI

## [2.1.0] - 2026-10-13

### Added

- Read input documents directly from binary paths

### Changed

- Update the PyO3 dependency and Rust bindings

## [2.0.1] - 2026-10-04

### Changed

- Update the underlying `carta` crate to 0.0.11

## [2.0.0] - 2026-09-30

### Added

- Support enabling and disabling format extensions in conversion options

### Changed

- **Breaking:** Control conversion extensions through explicit enable/disable options
- Simplify the conversion API and accept `Iterable` inputs where applicable

## [1.3.0] - 2026-08-29

### Changed

- Update the underlying `carta` crate to 0.0.10

## [1.2.0] - 2026-08-12

### Changed

- Update the underlying `carta` crate to 0.0.9

## [1.1.0] - 2026-08-08

### Added

- Convert from binary document formats
- Read input from buffered reader objects
- Add format aliases

## [1.0.0] - 2026-08-07

### Added

- Convert input from `pathlib.Path` objects

### Changed

- Refactor conversion methods to use the `.to_<format>()` naming convention

## [0.3.0] - 2026-08-07

### Added

- Pass conversion options through the Python API

### Changed

- Improve the CI and publishing workflows

## [0.2.0] - 2026-08-06

### Added

- Introduce the Python document-conversion API with format-specific conversion
  methods
- Separate text and binary conversion results


[2.1.5]: https://github.com/g-b-f/cartaPy/compare/2.1.4...HEAD
[2.1.4]: https://github.com/g-b-f/cartaPy/compare/v2.1.3...2.1.4
[2.1.3]: https://github.com/g-b-f/cartaPy/compare/v2.1.2...v2.1.3
[2.1.2]: https://github.com/g-b-f/cartaPy/compare/v2.1.1...v2.1.2
[2.1.1]: https://github.com/g-b-f/cartaPy/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/g-b-f/cartaPy/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/g-b-f/cartaPy/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/g-b-f/cartaPy/compare/v1.3.0...v2.0.0
[1.3.0]: https://github.com/g-b-f/cartaPy/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/g-b-f/cartaPy/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/g-b-f/cartaPy/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/g-b-f/cartaPy/compare/v0.3.0...v1.0.0
[0.3.0]: https://github.com/g-b-f/cartaPy/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/g-b-f/cartaPy/releases/tag/v0.2.0
