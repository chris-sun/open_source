json.array!(@locations) do |location|
  json.extract! location, :id, :name, :phone_number, :street1, :street2, :city, :state, :postal_code, :country_code, :latitude, :longitude
  json.url location_url(location, format: :json)
end
