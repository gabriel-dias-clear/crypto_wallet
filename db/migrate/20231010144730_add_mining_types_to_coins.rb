class AddMiningTypesToCoins < ActiveRecord::Migration[7.1]
  def change
    add_reference :coins, :mining_type, foreign_key: true
  end
end
