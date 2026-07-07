# Changelog

All notable changes to this project will be documented in this file.

## [0.7.0] - 2026-07-07

### Added
- Introduced BaseSplitter abstraction.
- Implemented RecursiveSplitter strategy.
- Added SplitterFactory with registry-based strategy selection.
- Added configurable chunk size and chunk overlap.
- Verified metadata preservation during document splitting.

## [0.6.0] - 2026-07-07

### Added
- Introduced `BaseLoader` abstraction.
- Implemented `PDFLoader` using LangChain `PyPDFLoader`.
- Added `LoaderFactory` with registry-based loader selection.
- Added structured logging for document loading.
- Verified extraction of `Document` objects and metadata.

## [0.5.0] - 2026-07-07

### Changed
- Introduced `LLMProvider` enum for type-safe provider selection.
- Replaced string-based provider comparisons with enum values.
- Updated configuration, factory, and provider implementations to use enums.
- Removed magic strings from the LLM architecture.

## [0.3.0] - 2026-07-06

### Added
- Implemented `BaseLLM` abstraction
- Added `LLMFactory` for provider creation
- Added first concrete provider: `GroqProvider`
- Integrated the framework with the Groq API
- Completed the first end-to-end LLM invocation through the provider architecture

## [0.1.0] - 2026-07-06

### Added
- Initial project structure
- Modular architecture
- Configuration system using Pydantic Settings
- Environment variable support via `.env`
- Git feature branch workflow