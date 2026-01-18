source "https://rubygems.org"

# Jekyll (compatible with GitHub Pages)
gem "jekyll", "~> 4.3"
gem "jekyll-sass-converter", "~> 3.0"
gem "sass-embedded", "~> 1.80"

# Local jekyll-text-theme gem (built from ../jekyll-text-theme)
gem "jekyll-text-theme", path: "../jekyll-text-theme"

# Jekyll plugins (required by jekyll-text-theme)
group :jekyll_plugins do
  gem "jemoji", "~> 0.8"        # Required by jekyll-text-theme
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-feed"
  gem "jekyll-paginate", "~> 1.1"
end

# Development and testing tools
group :development, :test do
  gem "html-proofer", "~> 5.2"
  gem "webrick", "~> 1.8"
end

# Windows and JRuby compatibility
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
