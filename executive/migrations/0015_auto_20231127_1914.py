# Generated by Django 4.2.6 on 2023-11-27 11:14

from django.db import migrations

def insert_data(apps, schema_editor):
    TableEight = apps.get_model('executive', 'TableEight')

    data = [
        ["Abalos, Karl Christian D."        , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Aquino, Rodolfo Y.  Jr."          , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Aribon, Mark Anthony R. III"      , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Bactasa, Melanie F."              , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Baltazar, Mary Ann Micah R., CPA" , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Banate, Richard B., CPA"          , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Bernardino, Abraham Seth R."      , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Bernardino, Girlie F."            , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Bulawit, Berna A."                , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Calingasan, Francisco S."         , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Castillo, Eleazar E."             , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Caturay, Norberto V., DEM"        , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Cecogo, Nieva M."                 , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Cipriano, Erwin"                  , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Clenuar, Ricardo H."              , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Cruz, Mary Grace I."              , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["De Leon, Celeste L."              , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Delmo, Elijah Paul B."            , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Dolorosa, Rodrigo S., DEM"        , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Domingo, Keinaz"                  , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Doromal, Cherry M."               , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Doromal, Roberto B."              , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Dungca, Leah A."                  , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Escober, Ain Gueul E."            , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Escober, Rosicar E., Ph.D."       , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Esguerra, Firmo A."               , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Esparagoza, Cherrylyn P."         , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Estella, Zandro T."               , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Fabela, Noel F."                  , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Fernandez, Alma C."               , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Administrative"  , "Serve on Curriculum Committee"           , "18"],
        ["Fulleros, Richard M."             , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Fulleros, Jorgen Z."              , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Gabasa, Asuncion V."              , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Garcia, Maita C."                 , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Gardon, Harold Q."                , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Gatan, Leslie O."                 , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Gatchalian, Irynne P."            , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Administrative"  , "Serve on Curriculum Committee"           , "18"],
        ["Gulmatico, Esther S., Ph.D."      , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Gutierrez, Jaime Jr. P."          , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Isip, John Robert F."             , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Lara, Erwin Vicman"               , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Leynes, Jerome Chrstopher G."     , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Monzon, Demelyn E. Ph.D"          , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Administrative"  , "Serve on Curriculum Committee"           , "18"],
        ["Monzon, Kezaiah M."               , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Morales, Sheryl R."               , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance"    , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Odpaga, Ernesto J., Jr."          , "1st Semester 22-23" , "INTE 40173 Capstone Project 2"                        , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Oliquino, Joanna Marie DC."       , "1st Semester 22-23" , "INTE-E3 IT Elective 3"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Pineda, Jose Gil C."              , "1st Semester 22-23" , "INTE-E4 IT Elective 4"                                , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Roxas, Rommel Y."                 , "1st Semester 22-23" , "COMP 20333 Social and Professional Issues in IT"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Servigon, Cleotilde B."           , "1st Semester 22-23" , "GEED 10013 Buhay at Mga Sinulat ni Rizal"             , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Soberano, Maricar O."             , "1st Semester 22-23" , "GEED 10083 Science, Technology and Society"           , "Research"        , "Conduct experiments for Project X"       , "18"],
        ["Soberano, Philip SJ."             , "1st Semester 22-23" , "INTE 30073 Information Assurance and Security 2"      , "Teaching"        , "Prepare lectures, grade assignments"     , "18"],
        ["Umali, Antonius C., DPA"          , "1st Semester 22-23" , "INTE 30083 Systems Administration and Maintenance",     "Teaching"        , "Prepare lectures, grade assignments"     , "18"]
    ]

    for item in data:
        TableEight.objects.create(
            workload_faculty  = item[0],
            workload_semester = item[1],
            workload_course   = item[2],
            workload_types    = item[3],
            workload_duties   = item[4],
            workload_total    = item[5], 
    )

class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0014_tableeight'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]
