class PagesController < ApplicationController
  include HighVoltage::StaticPage

  # def home
  #   Rails.logger.debug "Got here in HOME"
  #   @location = request.location
  # end

  def show
    Rails.logger.debug "THIS NOT BEING CALLED IS IT?"
    Rails.logger.debug "Got here in show"
    logger.debug "data: #{request.location.data}"
    logger.debug "IP: #{request.location.data['ip']}"
    @location = request.location
  end

end
