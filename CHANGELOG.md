# Changelog

All notable changes to this project will be documented in this file.

## [0.3.0] - 2026-07-06

### Added
- Implemented `BaseLLM` abstraction
- Added `LLMFactory` for provider creation
- Added first concrete provider: `GroqProvider`
- Integrated the framework with the Groq API
- Completed the first end-to-end LLM invocation through the provider architecture

## [0.1.0] - 06-07-2026

### Added
- Initial project structure
- Modular architecture
- Configuration system using Pydantic Settings
- Environment variable support via `.env`
- Git feature branch workflow