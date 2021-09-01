const {MongoClient} = require('mongodb');

async function main() {
    const uri = "mongodb+srv://root:Dunedin100@myfirstcluster.jekwe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

    const client = new MongoClient(uri);

    try {
        await client.connect();

        await findOneListingByName(client, "Test name");

    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
    }
  
}

main().catch(console.error);

async function findOneListingByName(client, nameOfCocktail) {
    const result = await client.db("CocktailTraining").collection("cocktail").findOne({name: nameOfCocktail});

    if (result){
        console.log(`Found a cocktail with the name '${nameOfCocktail}'`);
        console.log(result);
    } else {
        console.log(`No cocktail found with the name '${nameOfCocktail}'`);
    }
}


async function listDatabases(client) {
    const databasesList = await client.db().admin().listDatabases();

    console.log("Databases:");
    databasesList.databases.forEach(db => {
        console.log(`-${db.name}`);
    })
}