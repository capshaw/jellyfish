'use strict';

angular.module('app')
    .controller('EntryCtrl', function($scope, apiService) {

        var converter = new Showdown.converter();

        $scope.markdown = function (input) {
            if (input == null) {
                return;
            }

            var html = converter.makeHtml(input);
            var context = $('<div>' + html + '</div>');
            $('pre code', context).each(function (x, i) {
                var old_value = $(i).html();
                var new_value = hljs.highlightAuto(old_value).value;
                $(i).html(new_value);
            });
            return context.html();
        };

        $scope.deleteEntry = function (id, index) {
            apiService.deleteEntry(id).then(function(){
                $scope.deleted = true;
            })
        };
    })
    .directive('entry', function() {
        return {
            restrict: 'E',
            scope: {
                entry: '=entry',
                showOptions: '=showOptions'
            },
            controller: 'EntryCtrl',
            templateUrl: '/static/partials/entry.html'
        };
    });