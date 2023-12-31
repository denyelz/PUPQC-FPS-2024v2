# Generated by Django 4.2.6 on 2023-11-24 04:15

from django.db import migrations

def insert_data(apps, schema_editor):
    TableSix = apps.get_model('executive', 'TableSix')

    data = [  
        ["Abalos, Karl Christian D."        , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Aquino, Rodolfo Y.  Jr."          , "Compensatory Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Aribon, Mark Anthony R. III"      , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Bactasa, Melanie F."              , "Compensatory Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Baltazar, Mary Ann Micah R., CPA" , "Jury duty Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Banate, Richard B., CPA"          , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Bernardino, Abraham Seth R."      , "Unpaid Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Bernardino, Girlie F."            , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Bulawit, Berna A."                , "Annual Leave" 	 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Calingasan, Francisco S."         , "Leave Me Alone" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Castillo, Eleazar E."             , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Caturay, Norberto V., DEM"        , "Compensatory Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Cecogo, Nieva M."                 , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Cipriano, Erwin"                  , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Clenuar, Ricardo H."              , "Parental Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Cruz, Mary Grace I."              , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["De Leon, Celeste L."              , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Delmo, Elijah Paul B."            , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Dolorosa, Rodrigo S., DEM"        , "Study Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Domingo, Keinaz"                  , "Unpaid Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Doromal, Cherry M."               , "FMLA Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Doromal, Roberto B."              , "Compensatory Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Dungca, Leah A."                  , "Jury duty Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Escober, Ain Gueul E."            , "Annual Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Escober, Rosicar E., Ph.D."       , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Esguerra, Firmo A."               , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Esparagoza, Cherrylyn P."         , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Estella, Zandro T."               , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Fabela, Noel F."                  , "FMLA Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Fernandez, Alma C."               , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Fulleros, Richard M."             , "Jury duty Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Fulleros, Jorgen Z."              , "Study Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gabasa, Asuncion V."              , "Parental Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Garcia, Maita C."                 , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gardon, Harold Q."                , "FMLA Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gatan, Leslie O."                 , "Annual Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gatchalian, Irynne P."            , "ADA Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gulmatico, Esther S., Ph.D."      , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Gutierrez, Jaime Jr. P."          , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Isip, John Robert F."             , "Jury duty Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Lara, Erwin Vicman"               , "Leave" 			            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Leynes, Jerome Chrstopher G."     , "Annual Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Monzon, Demelyn E. Ph.D"          , "Study Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Monzon, Kezaiah M."               , "Maternity Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Morales, Sheryl R."               , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Odpaga, Ernesto J., Jr."          , "Marriage Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Oliquino, Joanna Marie DC."       , "Marriage Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Pineda, Jose Gil C."              , "Parental Leave" 		        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Roxas, Rommel Y."                 , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Servigon, Cleotilde B."           , "Maternity Leave" 	        , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Soberano, Maricar O."             , "Religious holidays Leave"    , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Soberano, Philip SJ."             , "ADA Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"],
        ["Umali, Antonius C., DPA"          , "Sick Leave" 		            , "2023-11-19", "2023-12-5", "31", "Pending"]
    ]

    for item in data:
        TableSix.objects.create(
            leave_faculty   = item[0],
            leave_type      = item[1],
            leave_start     = item[2],
            leave_end       = item[3],
            leave_duration  = item[4],
            leave_status    = item[5],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0010_tablesix'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]