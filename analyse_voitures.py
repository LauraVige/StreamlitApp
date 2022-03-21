import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(layout="centered", page_icon = ":car:")
st.markdown("""
<style>
body {
    color: #fff;
    background-color: #EB9797;
}
</style>
    """, unsafe_allow_html=True)


# Ajout titre
st.title('Analyse des caractéristiques des voitures entre 1972 et 1982')

url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)

# Markdown
st.markdown("### Analyse des données générales")

st.markdown("#### Répartition du nombre de modèles de voiture par continent")
viz = sns.countplot(x=df["continent"],
                order=df['continent'].value_counts(ascending=False).index)
st.pyplot(viz.figure, clear_figure = True)
st.write("Il y a beaucoup plus de modèles de voitures US dans le jeu de données.")

st.markdown("####  Analyse des données générales")
viz_correlation = sns.heatmap(df.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
                                annot=True)

st.pyplot(viz_correlation.figure, clear_figure = True)
st.write("On observe quelques correlations positives entre certaines features" + 
" relatives à la puissance des voitures. Et quelques correlations negatives entre ces mêmes features et le mpg")

viz3 = sns.barplot(data=df, x="continent", y="mpg")
st.pyplot(viz3.figure, clear_figure=True)

st.write("Ce sont les modèles américains qui consomment le plus. mpg petit = forte consommation")

st.markdown("### Analyse selon le continent")

status = st.radio("Choisissez une région : ", ('Europe', 'US', 'Japon'))

if (status == 'Europe'):
    df = df[df["continent"]==" Europe."]
elif (status == 'US'):
    df = df[df["continent"]==" US."]
else:
    df = df[df["continent"]==" Japan."]

st.write("Nombre de modèles par année : ")
viz4 = sns.histplot(data=df, x="year")
st.pyplot(viz4.figure, clear_figure = True)

st.write("Evolution de la puissance au cours des années.")

viz_correlation2 = sns.lineplot(data=df, x="year", y="hp", ci=None)
st.pyplot(viz_correlation2.figure, clear_figure = True)

st.write("On observe également une augmentation de la consommation des voitures au cours des années.")

viz_correlation3 = sns.lineplot(data=df, x="year", y="mpg", ci=None)
st.pyplot(viz_correlation3.figure, clear_figure = True)

st.write("Répartition de la consommation des modèles :")
st.write(pd.DataFrame(df["mpg"].describe()))

st.write("On observe une augmentation de la puissance au cours des années.")

viz_correlation4 = sns.lineplot(data=df, x="mpg", y="weightlbs", ci=None)
st.pyplot(viz_correlation4.figure, clear_figure = True)
