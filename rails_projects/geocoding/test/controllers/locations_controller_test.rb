require 'test_helper'

class LocationsControllerTest < ActionController::TestCase
  setup do
    @location = locations(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:locations)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create location" do
    assert_difference('Location.count') do
      post :create, location: { city: @location.city, country_code: @location.country_code, latitude: @location.latitude, longitude: @location.longitude, name: @location.name, phone_number: @location.phone_number, postal_code: @location.postal_code, state: @location.state, street1: @location.street1, street2: @location.street2 }
    end

    assert_redirected_to location_path(assigns(:location))
  end

  test "should show location" do
    get :show, id: @location
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @location
    assert_response :success
  end

  test "should update location" do
    patch :update, id: @location, location: { city: @location.city, country_code: @location.country_code, latitude: @location.latitude, longitude: @location.longitude, name: @location.name, phone_number: @location.phone_number, postal_code: @location.postal_code, state: @location.state, street1: @location.street1, street2: @location.street2 }
    assert_redirected_to location_path(assigns(:location))
  end

  test "should destroy location" do
    assert_difference('Location.count', -1) do
      delete :destroy, id: @location
    end

    assert_redirected_to locations_path
  end
end
