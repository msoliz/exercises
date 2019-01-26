var movies = [
    {name: "Interstellar", rating: 5, hasWatched: true},
    {name: "Guardians of the Galaxy", rating: 5, hasWatched: true},
    {name: "Iam legend", rating: 5, hasWatched: true}
];

movies.forEach(function(movies){   
    console.log(buildString(movies));
});

function buildString (movies){
    var result = "you have ";
    if(movies.hasWatched){
        result += "watched ";
    } else {
        result += "not seen ";
    }
    result += "\"" + movies.name + "\" - ";
    result += movies.rating + "stars";
    return result;
}

























