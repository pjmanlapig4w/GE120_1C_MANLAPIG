/*
GE120 Intro to OOP Geomatic Application
Peter John Manlapig
2023-21040

Exercise 5
*/ 

function getLatitude(distance, azimuth){
    /*
    compute for the latitude of the given line

    Input
    distance - float
    azimuth - float

    Output
    latitude - float
    */

    if (azimuth % 180 == 90) {return 0} 
    else {
    return (-distance * Math.cos(azimuth * Math.PI / 180.0))}

}
// lat = getLatitude(12, 45)
// console.log(lat)

function getDeparture(distance, azimuth){
    /*
    compute for the latitude of the given line

    Input
    distance - float
    azimuth - float

    Output
    departure - float
    */

    if (azimuth % 180 == 90) {return 0} 
    else {
    return (-distance * Math.sin(azimuth * Math.PI / 180.0))}
}
// dep = getDeparture(12, 45)
// console.log(dep)

function azimuthtoBearing(azimuth){
}

    // Create a sentinel controlled loop 
var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]

var lines = [];
var sumLat = 0;
var sumDep = 0;
var sumDist = 0;

for (var i = 0; i < data.length; i++){
    let line = data[i];
    let distance = line[0];
    let azimuth = line[1];

    let bearing = azimuthtoBearing(azimuth);
    let lat = getLatitude(distance, azimuth);
    let dep = getDeparture(distance, azimuth);

    sumLat += lat;
    sumDep += dep;
    sumDist += distance;

    lines.push([i, distance, bearing, lat, dep]);
}

console.log("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10));
for (var line of lines){
    console.log(
        line[0].toString().padEnd(10),
        line[1].toString().padEnd(10), 
        line[2].padEnd(15), 
        line[3].toFixed(5).toString().padEnd(10), 
        line[4].toFixed(5).toString().padEnd(10)
    );    
}

    // constCorrLat = -distance/sumDist * sumLat
    // constCorrDep = -distance/sumDist * sumDep 
    
    // corr_lat = constCorrLat* distance
    // corr_Dep = constCorrDep* distance

    // adjlat = lat + corr_lat
    // adjDep = dep + corr_Dep

    // let line = (counter, distance, bearing, round(lat, -3), round(dep, -3), round(corr_lat, -3), round(corr_Dep, -3), round(adjlat, -3), round(adjDep, -3))
    // lines.append(line)

    // yn = input("Add New Line? ")
    // if yn.lower() == "yes" or yn.lower()  == "y":
    //     counter = counter + 1
    //     continue
    // else:
    //     break

// console.log("\n\n")
// console.log("------------------------------------------------------------------------------------------")
// console.log('{: ^10} {: ^10} {: ^15} {: ^20} {: ^20}' .format ("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
// for line in lines:
//     console.log( '{: ^10} {: ^10} {: ^15} {: ^20} {: ^20}'.format(line[0], line[1], line[2], line[3], line[4]))

// console.log("------------------------------------------------------------------------------------------")

// console.log("\n\n")
// console.log("------------------------------------------------------------------------------------------")
// console.log('{: ^20} {: ^20} {: ^25} {: ^25}' .format ("LAT CORRECTION", "DEP CORRECTION", "ADJUSTED LATITUDE", "ADJUSTED DEPARTURE"))
// for line in lines:
//     console.log( '{: ^20} {: ^20} {: ^25} {: ^25}'.format(line[5], line[6], line[7], line[8]))
console.log("------------------------------------------------------------------------------------------")
console.log("\n\n")
console.log("SUMMATION OF LAT: ", sumLat.toPrecision(5))
console.log("SUMMATION OF DEP: ", sumDep.toPrecision(5))
console.log("SUMMATION OF DIS: ", sumDist.toPrecision(5))

lec = Math.sqrt(sumLat**2 + sumDep**2)

console.log("\n")
console.log("------------------------------------------------------------------------------------------")

console.log("LEC: ", lec.toPrecision(5))

rec = sumDist/lec
console.log("1: ", Math.floor(rec/1000))

console.log("\n")

console.log ("----------------------------------------END----------------------------------------------")