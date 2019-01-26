let movies = [
    {
    name: "Interstellar",
    rating: 5,
    hasWatched: true
    },
    {
    name: "Guardians of the Galaxy",
    rating: 5,
    hasWatched: true
    },
    {
    name: "Iam legend",
    rating: 5,
    hasWatched: true
    }
];

for (let item of movies) {
    let result = "You have ";
    if(movies.hasWatched){
        result += "watched ";
    } else {
        result += "not seen ";
    }
    result += "\"" + movies.name + "\" - " + movies.rating + " stars";
    console.log(result);
}




















