"""
Tests for the client module.
"""

from unittest.mock import Mock, patch

from floriday_supplier_client.client import Floriday, floriday, ApiWrapper


class MockApiClass:
    """Mock API class for testing."""

    def __init__(self, api_client):
        self.api_client = api_client

    def get_items_by_sequence_number(self, sequence_number, limit_result):
        """Mock method for testing."""
        return Mock(maximum_sequence_number=10, results=[])


class MockApiFactory:
    """Mock ApiFactory for testing."""

    def get_api_instance(self, api_class):
        """Mock method for testing."""
        return api_class(Mock())

    def get_api_client(self):
        """Mock method for testing."""
        return Mock()


@patch("floriday_supplier_client.client.ApiFactory")
def test_floriday_function(mock_api_factory):
    """Test the floriday function."""
    # Setup
    mock_api_factory.return_value = MockApiFactory()

    # Test creating a client
    client = floriday()
    assert isinstance(client, Floriday)

    # Test creating an API instance directly
    api = floriday(MockApiClass)
    assert isinstance(api, ApiWrapper)


@patch("floriday_supplier_client.client.ApiFactory")
def test_floriday_client_init(mock_api_factory):
    """Test Floriday client initialization."""
    # Setup
    mock_factory_instance = Mock()
    mock_api_factory.return_value = mock_factory_instance

    # Test with default options
    Floriday()
    mock_api_factory.assert_called_once()

    # Test with custom options
    _ = Floriday(
        client_id="test_id",
        client_secret="test_secret",
        api_key="test_key",
        auth_url="https://test.auth.url",
        base_url="https://test.base.url",
    )
    assert mock_api_factory.call_count == 2


@patch("floriday_supplier_client.client.ApiFactory")
def test_get_api(mock_api_factory):
    """Test get_api method."""
    # Setup
    mock_factory_instance = MockApiFactory()
    mock_api_factory.return_value = mock_factory_instance

    # Create a client
    client = Floriday()

    # Get an API instance
    api = client.get_api(MockApiClass)
    assert isinstance(api, ApiWrapper)

    # Get the same API instance again (should be cached)
    api2 = client.get_api(MockApiClass)
    assert api is api2


@patch("floriday_supplier_client.client.ApiFactory")
def test_refresh_token(mock_api_factory):
    """Test refresh_token method."""
    # Setup
    mock_factory_instance = Mock()
    mock_api_factory.return_value = mock_factory_instance

    # Create a client
    client = Floriday()

    # Get an API instance to populate the cache
    client._api_cache["MockApiClass"] = Mock()

    # Refresh the token
    client.refresh_token()

    # Verify the token was refreshed
    assert mock_factory_instance._get_access_token.called
    assert mock_factory_instance._configure_client.called

    # Verify the API cache was cleared
    assert not client._api_cache


@patch("floriday_supplier_client.client.ApiFactory")
def test_context_manager(mock_api_factory):
    """Test context manager support."""
    # Setup
    mock_factory_instance = Mock()
    mock_api_factory.return_value = mock_factory_instance

    # Use the client as a context manager
    with Floriday() as client:
        # Get an API instance to populate the cache
        client._api_cache["MockApiClass"] = Mock()

    # Verify the API cache was cleared
    assert not client._api_cache


@patch("floriday_supplier_client.client.sync_entities")
def test_api_wrapper_sync(mock_sync_entities):
    """Test ApiWrapper sync method."""
    # Setup
    mock_api_instance = MockApiClass(Mock())
    mock_client = Mock()

    # Create an API wrapper
    wrapper = ApiWrapper(mock_api_instance, mock_client)
    
    # Mock the _find_sequence_method to return a mock function
    mock_fetch = Mock()
    wrapper._find_sequence_method = Mock(return_value=mock_fetch)
    
    # Call sync
    wrapper.sync(start_seq=0, on_item=lambda x: x)
    
    # Verify sync_entities was called
    mock_sync_entities.assert_called_once()


@patch("floriday_supplier_client.client.EntitySynchronizer")
def test_api_wrapper_create_sync(mock_entity_synchronizer):
    """Test ApiWrapper create_sync method."""
    # Setup
    mock_api_instance = MockApiClass(Mock())
    mock_client = Mock()
    mock_synchronizer = Mock()
    mock_entity_synchronizer.return_value = mock_synchronizer

    # Create an API wrapper
    wrapper = ApiWrapper(mock_api_instance, mock_client)
    
    # Mock the _find_sequence_method to return a mock function
    mock_fetch = Mock()
    wrapper._find_sequence_method = Mock(return_value=mock_fetch)

    # Call create_sync
    result = wrapper.create_sync(start_seq=0)

    # Verify EntitySynchronizer was created
    mock_entity_synchronizer.assert_called_once()
    assert result is mock_synchronizer


# Test for sync_iter will be added in a future increment
