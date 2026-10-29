require_relative "lib/crawlora/vlr/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-vlr"
  spec.version = Crawlora::Vlr::VERSION
  spec.summary = "VLR.gg API client for Crawlora (23 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted VLR.gg API. Covers Valorant matches, events, results, rankings, statistics, news, and forum data across 23 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=vlr-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-vlr", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-vlr/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
