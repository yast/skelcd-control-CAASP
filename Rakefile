require "yast/rake"

Yast::Tasks.submit_to((ENV["YAST_SUBMIT"] || :casp10).to_sym)
obs_project = "Devel:YaST:CASP:1.0"

Yast::Tasks.configuration do |conf|
  #lets ignore license check for now
  conf.skip_license_check << /.*/
end
