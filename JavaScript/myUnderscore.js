// This is a collection of implementations of the underscore js common functions
// http://underscorejs.org/

function pEach(l, cb){
    if (Array.isArray(l)){
        for (var i = 0; i < l.length; i++) cb(l[i]);
    }
    else {
        var k = Object.keys(l);
        for (var i = 0; i < k.length; i++) cb(l[k[i]]);
    }
}

function find(l, pred){
    var ans;
    pEach(l, function(x){
        //console.log(pred(x));
        if (pred(x)) {
            ans = x;
            return;
        }
    });
    return ans;

}

function filter(l, pred){
    var ans = [];
    pEach(l, function(x){
        if (pred(x)) ans.push(x);
    });
    return ans;
}

function where(l, prop){
    var ans = [];
    pEach(l, function(x){
        for (var k in prop){
            if (Object.keys(x).indexOf(k) < 0 || x[k] !== prop[k]) return false;
        }
        ans.push(x);
    });
    return ans;

}

function whereFind(l, prop){
    var ans, found = false;
    pEach(l, function(x){
        for (var k in prop){
            if (found || Object.keys(x).indexOf(k) < 0 || x[k] !== prop[k]) return false;
        }
        found = true;
        ans = x;
    });
    return ans;
}

// where and/or whereFind tests:
/*

var test01 = { a: 1, b: 2, c: 3 };
var test02 = { a: 2, b: 2, c: 3 };
var lst = [test01, test02];
console.log(whereFind(lst, {b: 2, c: 3}));
console.log(whereFind(lst, {a: 2, c: 3}));
console.log(whereFind(lst, {b: 3, c: 3}));
*/

function reject(list, predicate){
    var ans = [];
    pEach(list, function(x){
        if (!predicate(x)) ans.push(x);
    });
    return ans;
}

// console.log(reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; }));

function every(list, predicate){
    var ans = true;
    pEach(list, function(x){
        if (!predicate && !x) ans = false;
        else if (predicate && !predicate(x)) ans = false;
    });
    return ans;
}
// console.log(every([true, 1, 'yes']));

function any(list, predicate){
    for (var i = 0; i < list.length; i++){
        if (typeof predicate === 'function' && predicate(list[i])) return true;
    }
    return false;
}

//console.log(any([1,3,5,7,9,11,13,15,17,19,21,23], function(x){ return x%2 == 0; }))

function contains(list, value, fromIndex){
    return list.indexOf(value) >= 0 ? true : false;
}

// console.log(contains([1,2,3,4,5], 3));
// console.log(contains([1,2,3,4,5], 6));

function map(list, cb){
    var ans = [];
    pEach(list, function(x){
        ans.push(cb(x));
    });
    return ans;
}

function pluck(objList, propName){
     return map(objList, function(x){
        console.log(x[propName]);
         return x[propName];
    });

}

// var stooges = [{name: 'moe', age: 40}, {name: 'larry', age: 50}, {name: 'curly', age: 60}];
// console.log(pluck(stooges, 'name'));

function max(list, iteratee){
    var ans = list[0];
    pEach(list, function(x){
        if (typeof iteratee === 'function'){
            if (iteratee(x) > iteratee(ans)){
                ans = x;
            }
        }
        else if (x > ans) ans = x;
    });
    return ans;
}

// var stooges = [{name: 'moe', age: 40}, {name: 'larry', age: 50}, {name: 'curly', age: 60}];
// console.log(max(stooges, function(stooge){ return stooge.age; }));
// console.log(max([5,2,8,4,7,3,2,5,7,34,2,0]));

function min(list, iteratee){
    iteratee = iteratee || function(x){ return x; }
    return max(list, function(x){return -iteratee(x);});
}

// var stooges = [{name: 'moe', age: 40}, {name: 'larry', age: 30}, {name: 'curly', age: 60}];
// console.log(min(stooges, function(stooge){ return stooge.age; }));
// console.log(min([5,2,8,4,7,3,2,5,-7,34,2,0]));

function sortedInsert(list, value, iteratee){
    iteratee = iteratee || function(x){return x;}
    for (var i = 0; i < list.length; i++){
        if (iteratee(value) <= iteratee(list[i])){
            //i -= 1;
            break;
        }
    }
    list.splice(i, 0, value);
    return list;
}

// console.log(sortedInsert([1,2,3,5], 4));
// console.log(sortedInsert([2, 3, 4], 1));
// console.log(sortedInsert([], 2));

function sortBy(list, iteratee){
    var ans = [];
    iteratee = iteratee || function(x){ return x; }
    pEach(list, function(x){
        ans = sortedInsert(ans, x, iteratee);
    });
    return ans;
}

// console.log(sortBy([1, 2, 3, 4, 5, 6], function(num){ return Math.sin(num); }));

function groupBy(list, iteratee){
    var res = {};
    pEach(list, function(x){
        if (Object.keys(res).indexOf(iteratee(x)) < 0) res[iteratee(x)] = [];
        res[iteratee(x)].push(x);
    });
    return res;
}

// console.log(groupBy([2.1, 3.8, 1.1, 4.5, 2.6, 3.2, 2.7], function(x){ return ''+Math.floor(x); }));
// console.log(groupBy(['paul','pat','xina'], function(x){ return ''+x.length; }));

function shuffle(list){
    for (var i = list.length-1; i>=0; i--) {
        var r = Math.floor(Math.random()*i);
        var temp = list[i];
        list[i] = list[r];
        list[r] = temp;
    }
}

// var l = [1,2,3,4,5];
// shuffle(l);
// console.log(l);

function sample(list, n){
    n = n || 1;
    var tl = list.slice(); // gotta do it this way, var tl = list is copy by reference
    var res = [];
    for (var i = 0; i < n; i++){
        var selection = Math.floor(Math.random()*tl.length);
        res.push(tl.splice(selection, 1));
    }
    return res;
}

// var l = [1,2,3,4,5];
// console.log(sample(l, 5));
// console.log(sample(l));

function isOdd(x){ return x%2 === 1; }
function partition(list, predicate){
    var trues = [];
    var falses = [];
    pEach(list, function(x){
        if (predicate(x)) trues.push(x);
        else falses.push(x);
    });
    return [trues, falses];
}

// console.log(partition([0,1,2,3,4,5], isOdd));

function first(array, n){
    n = n || 1;
    var res = [];
    for (var i = 0; i < n; i++){
        res.push(array[i]);
    }
    return res;
}
// console.log(first([1,2,3,4,5],2));

function initial(array, n){
    n = n || 1;
    return first(array, array.length-n);
}

//console.log(initial([1,2,3,4,5]));

function last(array, n){
    n = n || 1;
    var res = [];
    for (var i = array.length-1; i > array.length-n-1; i--){
        res.unshift(array[i]);
    }
    return res;
}
// console.log(last([1,2,3,4,5], 3));

function rest(array, index){
    index = index || 1;
    return last(array, array.length-index);
}

// console.log(rest([1,2,3,4,5], 3));

function compact(array){
    var res = [];
    pEach(array, function(x){ if (x) res.push(x); });
    return res;
}

// console.log(compact([0, 1, false, 2, '', 3]));



function flatten(array, shallow){
    var res = [];
    if (shallow){
        pEach(array, function(x){
            if (Array.isArray(x)){
                pEach(x, function(y){
                    res.push(y);
                });
            }
            else { res.push(x); }
        });
    }
    else {
        for (var i = 0; i < array.length; i++){
        value = array[i];
        if (Array.isArray(value)) {
            value = flatten(value, shallow);
            for (var j = 0; j < value.length; j++){
                res.push(value[j]);
            }
        }
        else {res.push(value);}
    }

    }
    return res;


}

// console.log(flatten([1, [2], [3, [[4]]]]));
// console.log(flatten([1, [2], [3, [[4]]]], true));


function toArray(list){
    var res = [];
    for (var i = 0; i < list.length; i++){
        res.push(list[i]);
    }
    return res;
}

// console.log((function(){ return toArray(arguments).slice(1); })(1, 2, 3, 4));

function without(array){
    var res = [];
    var values = toArray(arguments).slice(1);
    pEach(array, function(x){
        if (values.indexOf(x) < 0) res.push(x);
    });
    return res;
}

// console.log(without([1,2,3,6,7,2,3,4,6,7,8,2,5,7,8,3,5,7,2,7,3,5,3,4],2,3,4,5));

function union(){
    var vals = toArray(arguments);
    var res = [];
    pEach(vals, function(x){
        pEach(x, function(y){
            if (res.indexOf(y) < 0) res.push(y);
        });
    });
    return res;
}
// console.log(union([1, 2, 3], [101, 2, 1, 10], [2, 1]));

function intersection(){
    var res = arguments[0].slice();
    var vals = toArray(arguments).slice(1);
    for (var i = 0; i < vals.length; i++){
        for (var j = 0; j < res.length; j++){
            if (vals[i].indexOf(res[j]) < 0) { res.splice(j, 1); }
        }
    }
    return res;
}

// console.log(intersection([1, 2, 3], [101, 2, 1, 10], [2, 1]));

function difference(array){
    var vals = toArray(arguments).slice(1);
    var res = array.slice();
    for (var i = 0; i < vals.length; i++){
        for (var j = 0; j < res.length; j++){
            if (vals[i].indexOf(res[j]) >= 0) {res.splice(j, 1);}
        }
    }
    return res;
}

// console.log(difference([1, 2, 3, 4, 5], [5, 2, 10]));

function uniq(array, isSorted, iteratee){
    var res = [array[0]];
    console.log(array);
    iteratee = iteratee || function(x){ return x; }
    if (isSorted) {
        console.log('a');
        for (var i = 1; i < array.length; i++){
            if (iteratee(array[i]) !== iteratee(res[res.length-1])) res.push(array[i]);
        }
    }
    else {
        console.log('b');
        for (var i = 1; i < array.length; i++){
            if (res.indexOf(array[i]) < 0) res.push(array[i]);
        }
    }
    return res;
}

//console.log(uniq([1, 2, 1, 4, 1, 3]));

function zip(){
    var res = [], input = toArray(arguments), maxL = 0;
    pEach(input, function(x){
        if (x.length > maxL) maxL = x.length;
    });
    for (var i = 0; i < maxL; i++){
        res.push([]);
    }
    for (var i = 0; i < input.length; i++){
        for (var j = 0; j < maxL; j++){
            res[j][i] = input[i][j];
        }
    }
    return res;
}

//console.log(zip(['moe', 'larry', 'curly'], [30, 40, 50], [true, false, false]));

function object(list, values){
    var res = {};
    if (values) {
        for (var i = 0; i < list.length; i++){
            res[list[i]] = values[i];
        }
    }
    else {
        pEach(list, function(x){
            res[x[0]] = x[1];
        });
    }
    return res;
}

//console.log(object(['moe', 'larry', 'curly'], [30, 40, 50]));
//console.log(object([['moe', 30], ['larry', 40], ['curly', 50]]));

function indexOf(array, value, isSorted){
    if (isSorted === true) {
        var step = Math.round(array.length/4), idx = Math.round(array.length/2);
        while (array[idx] !== value){
            if (step === 0) return -1;
            if (array[idx] > value) {
                idx -= step;
            }
            else {
                idx += step;
            }
            step = Math.round(step/2);
        }
        return idx;
    }
    else {
        isSorted = isSorted || 0;
        for (var i = isSorted; i < array.length; i++){
            if (array[i] === value) return i;
        }
        return -1;
    }
}

//console.log(indexOf([1, 2, 3, 4, 5], 4));

function lastIndexOf(array, value, fromIndex){
    for (var i = fromIndex || array.length-1; i >= 0; i--){
        if (array[i] === value) return i;
    }
    return -1;
}

//console.log(lastIndexOf([1,2,3,1,2,3,1,2,3,1], 2));
//console.log(lastIndexOf([1,2,3,1,2,3,1,2,3,1], 2, 6));

function sortedIndex(list, value, iteratee){
    iteratee = iteratee || function(x) { return x; }
    var idx = Math.round(list.length/2);
    while (true){
        //console.log(idx);
        //console.log(iteratee(list[idx]));
        if (iteratee(list[idx]) === iteratee(value)) return idx;
        else if (iteratee(list[idx]) > iteratee(value)) {
            if (idx === 0) return idx;
            if (iteratee(list[idx-1]) < iteratee(value)) return idx;
            idx = Math.floor(idx/2);
        }
        else if (iteratee(list[idx]) < iteratee(value)) {
            if (idx === list.length-1) return idx+1;
            if (iteratee(list[idx+1]) > iteratee(value)) return idx+1;
            idx = Math.round( (idx+(list.length-1))/2   );
        }
    }
}

//console.log(sortedIndex([10, 20, 30, 40, 50], 5));
//console.log(sortedIndex([10, 20, 30, 40, 50], 15));
//console.log(sortedIndex([10, 20, 30, 40, 50], 25));
//console.log(sortedIndex([10, 20, 30, 40, 50], 35));
//console.log(sortedIndex([10, 20, 30, 40, 50], 45));
//console.log(sortedIndex([10, 20, 30, 40, 50], 55));

function range(start, stop, step){
    if (arguments.length === 1) {
        stop = start;
        start = 0;
    }
    step = step || 1;
    var res = [];
    for (var i = start; step/Math.abs(step)*i < step/Math.abs(step)*stop; i += step){
        res.push(i);
    }
    return res;
}
/*
console.log(range(10));
console.log(range(1,10));
console.log(range(1, 10, 5));
console.log(range(1, -10, -2))
console.log(range(10, 1));
*/

function bind(cb, obj, greeting){
    return function() {return cb.call(obj, greeting);}

}

// var func = function(greeting){ return greeting + ': ' + this.name };
// func = bind(func, {name: 'moe'}, 'hi');
// console.log(func());

function sub(x){
    return function(y){
        return y - x;
    }
}

function partial(cb){
    if (arguments[1] === '_'){
        var i = arguments[2];
        return function(x){ return cb(x, i);}
    }
    var i = arguments[1];
    return function(x){ return cb(i, x);}
}

/*
var subtract = function(a, b) { return b - a; };
sub5 = partial(subtract, 5);
console.log(sub5(20));
subFrom20 = partial(subtract, '_', 20);
console.log(subFrom20(5));
*/

/*
var sub5 = sub(5);
console.log(sub5(20));
*/

var once = function(cb){
    var executed = false;
    return function(){
        if (!executed){
            executed = true;
            cb(x);
        }
    }
};

//var a = once( function(x){ console.log(10-x); } );
//for (var x = 3; x > 2; x--){ a(x); }

var after = function(count, cb){
    var runs = 0;
    return function(x){
        runs++;
        if (runs >= count){
            cb(x);
        }
    }
}

//var b = after( 3, function(x){ console.log(10+x); } );
//for (var x = 0; x < 10; x++){ b(x); }

function before(count, cb){
    var runs = 0;
    var ans;
    return function(x){
        runs++;
        if (runs === 3) ans = cb(x);
        if (runs >= 3) return ans;
        else { return cb(x); }
    }
}

//var c = before( 3, function(x){ return 10+x; });
//for (var i = 0; i < 5; i++) console.log(c(i));

function negate(cb){
    return function(x){
        return !cb(x);
    }
}

//var isFalsy = negate(Boolean);
//for (var i = -2; i < 2; i++) console.log(isFalsy(i));

function compose(){
    var i = arguments;
    return function(x){
        var ans = x;
        for (var j = i.length-1; j >= 0; j--){
            //console.log(j);
            ans = i[j](ans);
        }
        return ans;
    }
}

/*
var greet    = function(name){ return "hi: " + name; };
var exclaim  = function(statement){ return statement.toUpperCase() + "!"; };
var welcome  = compose(greet, exclaim);
console.log(welcome('moe'));
*/

function keys(obj){
    var k = [];
    for (var i in obj) { k.push(i); }
    return k;
}

//console.log(keys({ one: 1, two: 2, three: 3 }));

function values(obj){
    var v = [];
    for (var i in obj) { v.push(obj[i]); }
    return v;
}

// console.log(values({ one: 1, two: 2, three: 3 }));
