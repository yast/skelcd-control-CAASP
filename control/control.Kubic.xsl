<!--
  Definition of the control.CAASP.xml -> control.Kubic.xml transformation.
-->

<xsl:stylesheet version="1.0" xmlns:n="http://www.suse.com/1.0/yast2ns" xmlns:config="http://www.suse.com/1.0/configns" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="xml" indent="yes"/>

  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>

  <!-- remove the "container-feeder" service from all roles (not available in Kubic) -->
  <xsl:template match="n:system_role/n:services/n:service[n:name='container-feeder']"/>
  <!-- a trick to remove the remaining empty line after node removal -->
  <xsl:template match="text()[following-sibling::node()[1][self::n:service[n:name='container-feeder']]]" />

  <!-- remove the "admin-node-setup" service from all roles (not available in Kubic) -->
  <xsl:template match="n:system_role/n:services/n:service[n:name='admin-node-setup']"/>
  <!-- a trick to remove the remaining empty line after node removal -->
  <xsl:template match="text()[following-sibling::node()[1][self::n:service[n:name='admin-node-setup']]]" />

  <!-- Add the "extra_urls" part from the normal openSUSE control file -->
  <xsl:template match="n:software">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
      <!-- Make sure this is the openSUSE control file! -->
      <xsl:copy-of select="document('/CD1/control.xml')/*/n:software/n:extra_urls"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
