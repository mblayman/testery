import DS from 'ember-data';

export default DS.Model.extend({
  passes: DS.attr('number', { defaultValue: 0 }),
});
