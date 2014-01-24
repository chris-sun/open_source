class Location < ActiveRecord::Base
  geocoded_by :full_street_address
  after_validation :geocode          # auto-fetch coordinates

  def full_street_address
    return "#{self.street1}, #{self.city}, #{self.state}, #{self.country_code}, #{self.postal_code}"
  end

end
