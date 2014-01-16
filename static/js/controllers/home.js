'use strict';

angular.module('app')
    .controller('HomeCtrl', function ($scope, apiService) {
        $scope.page = 1;
        $scope.total_pages = -1;
        $scope.entries = [];

        $scope.loadMoreEntries = function () {
            if ($scope.page > $scope.total_pages && $scope.total_pages != -1) {
                return;
            }

            apiService.getEntries($scope.page++).then(function(data){
                $scope.total_pages = data.total_pages;
                $scope.entries = $scope.entries.concat(data.entries);
            });
        };

        $scope.loadMoreEntries();
    });