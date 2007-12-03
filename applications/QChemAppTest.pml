<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="QChemApp">
        <property name="quantumEngine">QChem</property>
        <property name="General Settings">GeneralSettings</property>

        <component name="QChem">
            <facility name="Sample">Sample</facility>
            <property name="Property Sampling Frequency (fs)">4.0</property>

            <component name="Sample">
                <property name="Crystal Structure">UnitCellBuilder</property>

                <component name="UnitCellBuilder">
                    <property name="Unit Cell">UnitCell</property>

                    <component name="UnitCell">
                        <property name="spaceGroup">None</property>
                    </component>

                </component>

            </component>

        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Sun Jul  1 13:16:03 2007-->

<!-- End of file -->
