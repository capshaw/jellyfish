'use strict';

angular.module('client')
    .controller('HomeCtrl', function ($scope, $http) {

        var base_url = 'http://127.0.0.1:5000';
        var user = 1;
        var converter = new Showdown.converter();

        $scope.getFeed = function (user, page) {
            $scope.url = base_url + '/feed/' + user + '/' + page;

            $http({method: 'GET', url: $scope.url}).
                success(function(data, status, headers, config) {
                    $scope.entries = data.feed;
                    $scope.page = data.page;
                    $scope.totalPages = data.total_pages;
                }).
                error(function(data, status, headers, config) {
                    console.log('There was an error fetching data.');
                });
        };

        $scope.markdown = function (input) {
            if (input == null) {
                return '';
            }
            return converter.makeHtml(input);
        };

        $scope.previousPage = function () {
            $scope.getFeed(user, $scope.page - 1);
        };

        $scope.nextPage = function () {
            $scope.getFeed(user, $scope.page + 1);
        };

        $scope.getFeed(user, 1);
    });