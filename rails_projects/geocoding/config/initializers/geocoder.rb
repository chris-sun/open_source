Geocoder.configure(
  # geocoding service (see below for supported options):
  :lookup => :google,

  # IP address geocoding service (see below for supported options):
  :ip_lookup => :freegeoip,

  # to use an API key:
  #:api_key => "AIzaSyAP5hPsvmeXYT7-GJxA0CODhD8x6Wto4UY",

  # geocoding service request timeout, in seconds (default 3):
  :timeout => 5,

  # set default units to miles:
  :units => :mi,

  # caching (see below for details):
  #:cache => nil
  #:cache_prefix => "geocoder"
)
