# Doing

## Goal

Move the generic entity synchronization code from vine-floriday-adapter to floriday-supplier-client to make it available for other projects using the client library.

## Analysis

The current situation:

- Generic sync code exists in vine-floriday-adapter's sync.py
- The code provides a reusable pattern for synchronizing Floriday entities using sequence numbers
- Key components:
  - `sync_entities` function that handles the synchronization workflow
  - Takes callbacks for entity-specific operations (get_by_sequence, persist_entity)
  - Manages pagination and sequence number tracking
  - Includes basic rate limiting (0.5s sleep between requests)
- The code is independent of vine-floriday-adapter specific concerns
- Current implementation relies on external persistence layer through get_max_sequence_number

## Design

Proposed solution:

1. Create a new module in floriday-supplier-client for synchronization:

   ```python
   floriday_supplier_client/
   └── sync/
       ├── __init__.py
       └── entity_sync.py  # Contains the sync functionality
   ```

2. Enhance the sync_entities function:
   - Make it more Pythonic with type hints
   - Add proper error handling
   - Make rate limiting configurable
   - Make persistence optional (allow in-memory tracking)
   - Add logging instead of print statements
   - Add docstrings and examples

3. Add tests:
   - Unit tests for sync logic
   - Integration tests with mock API responses
   - Example usage in documentation

4. Update documentation:
   - Add sync module documentation
   - Include example usage
   - Document configuration options

## Steps

1. Create new sync module structure in floriday-supplier-client
2. Implement enhanced sync_entities function
3. Add comprehensive test suite
4. Update documentation
5. Create example usage
6. Create issue in vine-floriday-adapter project:
   - Document how to migrate to the new sync function
   - Provide example code showing the migration path
   - Include any breaking changes and required updates

## Progress

- [ ] Step 1: Create module structure
- [ ] Step 2: Implement sync_entities
- [ ] Step 3: Add tests
- [ ] Step 4: Update documentation
- [ ] Step 5: Create examples
- [ ] Step 6: Create migration guide issue
