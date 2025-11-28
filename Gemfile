source "https://rubygems.org"

# Core Jekyll
gem "jekyll", "~> 4.3.4"

# ----------------------------------------------------
# SEO & TRAFFIC DOMINANCE PLUGINS
# ----------------------------------------------------
group :jekyll_plugins do
  
  # AUTOMATIC SITEMAP (Critical)
  # This builds the sitemap.xml file Google needs to index you.
  gem "jekyll-sitemap"
  
  # RSS FEED
  # Creates feed.xml so people can subscribe.
  gem "jekyll-feed"
  
  # PAGINATION (Optional but good for scalability)
  # Helps if you eventually have 100+ reviews.
  gem "jekyll-paginate"

end

# ----------------------------------------------------
# LINUX / RUBY 3.0+ COMPATIBILITY
# ----------------------------------------------------
# You need this to run 'jekyll serve' on modern Linux.
# Without it, the server will crash.
gem "webrick"
