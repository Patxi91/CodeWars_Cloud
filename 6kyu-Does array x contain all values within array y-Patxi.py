class Array
  def contains_all?(other_array)
    other_array.all? { |item| self.include?(item) }
  end
end
