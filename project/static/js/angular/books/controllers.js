(function () {
     "use strict";
}());


MyApp.service('getBooks', function ($http) {
    this.getData = function () {
        var promise = $http({method:'GET', url:'/api/books/'})
            .success(function (data, status, headers, config) {
                return data;
            })
            .error(function (data, status, headers, config) {
                console.log("Could not get books data.")
            });

        return promise;
    }
});



MyApp.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/book/:bookId',
            {
                templateUrl: 'book-detail.html',
                controller: 'BooksCtrl'
            })
        .when('/books/',
            {
                templateUrl: 'books-list.html',
                controller: 'BooksCtrl'
            })
        .otherwise(
            {
                redirectTo: '/'
            }
      );
}]);



MyApp.controller('BooksCtrl', ['$scope', '$filter', 'getBooks', function($scope, filter, getBooks) {

    getBooks.getData().then(function(promise){
        $scope.books=promise.data.results;
    });

}]);
