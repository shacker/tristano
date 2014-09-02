(function () {
     "use strict";
}());


// Get list of books from API
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


// Get single book from API
MyApp.service('getBook', function ($http) {
    this.getData = function (bookId) {
        var promise = $http({method:'GET', url:'/api/books/' + bookId})
            .success(function (data, status, headers, config) {
                return data;
            })
            .error(function (data, status, headers, config) {
                console.log("Could not get book data.")
            });

        return promise;
    }
});



MyApp.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
    $routeProvider
        .when('/:bookId',
            {
                templateUrl: '/static/js/angular/books/partials/books-detail.html',
                controller: 'BooksDetailCtrl'
            })
        .when('/',
            {
                templateUrl: '/static/js/angular/books/partials/books-list.html',
                controller: 'BooksListCtrl'
            })
        .otherwise(
            {
                redirectTo: '/'
            }
      );
}]);



MyApp.controller('BooksListCtrl', ['$scope', '$filter', 'getBooks', function($scope, filter, getBooks) {

    getBooks.getData().then(function(promise){
        $scope.books=promise.data.results;
    });

}]);


MyApp.controller('BooksDetailCtrl', ['$scope', '$routeParams', '$filter', 'getBook', function($scope, $routeParams, filter, getBook) {

    getBook.getData($routeParams.bookId).then(function(promise){
        $scope.book=promise.data;
    });

}]);
