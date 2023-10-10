class WelcomeController < ApplicationController
  def index()
    @nome = params[:nome]
    if !@nome
      @nome = 'Anônimo'
    end
  end
end
