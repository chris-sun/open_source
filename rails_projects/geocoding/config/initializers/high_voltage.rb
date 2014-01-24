# config/initializers/high_voltage.rb
HighVoltage.configure do |config|
  config.home_page = 'home'
  # for URLs like "/about", look for view files in "pages/about"
  # Eliminate need for URLs like "/pages/about"
  config.route_drawer = HighVoltage::RouteDrawers::Root
end
