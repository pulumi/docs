module ReplaceRegexFilter
  def replace_regex(input, regex, replacement = '')
    input.gsub(Regexp.new(regex), replacement.to_s)
  end
end
Liquid::Template.register_filter(ReplaceRegexFilter)
