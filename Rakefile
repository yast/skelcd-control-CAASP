require "yast/rake"

Yast::Tasks.configuration do |conf|
  # internal OBS
  conf.obs_api = "https://api.suse.de/"
  conf.obs_project = "Devel:YaST:CASP:1.0"
  conf.obs_target = "CASP_1.0"
  conf.obs_sr_project = "SUSE:SLE-12-SP2:Update:Products:CASP10"

  # lets ignore license check for now
  conf.skip_license_check << /.*/
end

