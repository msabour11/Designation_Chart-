// original
frappe.pages["designation-chart"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: __('Designation Chart'),
    single_column: true,
  });
/////////////

// this.show=function() {
//   // this.setup_actions();
//   if (this.page.main.find('[data-fieldname="department"]').length) return;
//   let me = this;

//   let department = this.page.add_field({
//     fieldtype: 'Link',
//     options: 'Department',
//     fieldname: 'department',
//     placeholder: __('Select Company'),
//     only_select: true,
//     // reqd: 1,
//     change: () => {
//       me.department = '';
//       $('#hierarchy-chart-wrapper').remove();

//       // Correctly access the department field value
//       let departmentValue = me.page.fields_dict['department'].get_value();

//       if (departmentValue) {
//         me.department = departmentValue;

//         console.log(departmentValue)

//         // svg for connectors
//         // me.make_svg_markers();
//         // me.setup_hierarchy();
//         // me.render_root_nodes();
//         // me.all_nodes_expanded = false;
//       }
//       // else {
//       //   frappe.throw(__('Please select a company first.'));
//       // }
//     }
//   });

//   department.refresh();
//   $(`[data-fieldname="department"]`).trigger('change');
//   $(`[data-fieldname="department"] .link-field`).css('z-index', 2);
// };

////////////
  $(wrapper).bind("show", () => {
    frappe.require("hierarchy-chart.bundle.js", () => {
      let method =
        "designation.designation.page.designation_chart.designation_chart.get_children";

      let designation_chart;
      designation_chart = new hrms.HierarchyChart(
        "Designation",
        wrapper,
        method
      );

      if (frappe.is_mobile()) {
        designation_chart = new hrms.HierarchyChartMobile(
          "Designation",
          wrapper,
          method
        );
      } else {
        designation_chart = new hrms.HierarchyChart(
          "Designation",
          wrapper,
          method
        );
      }

      frappe.breadcrumbs.add("HR");
      designation_chart.show();
    });
  });
};

// work selected
// frappe.pages['designation-chart'].on_page_load = function(wrapper) {
//   var page = frappe.ui.make_app_page({
//       parent: wrapper,
//       title: __('Designation Chart'),
//       single_column: true
//   });

//   // Create a placeholder for the department field
//   let department_field_wrapper = $(wrapper).find('.department-field-wrapper');
//   if (!department_field_wrapper.length) {
//       department_field_wrapper = $('<div class="department-field-wrapper" style="padding: 15px;"></div>').appendTo(page.main);
//   }


//   // Render the department input
//   department_field.refresh();

//   // Function to load the chart
//   function load_chart(wrapper, department) {
//       $(wrapper).unbind("show").bind("show", function() {
//           frappe.require("hierarchy-chart.bundle.js", function() {
//               let method = "designation.designation.page.designation_chart.designation_chart.get_children";
//               let args = { department: department }; // Include department in args

//               let designation_chart;
//               if (frappe.is_mobile()) {
//                   designation_chart = new hrms.HierarchyChartMobile(
//                       "Designation",
//                       wrapper,
//                       method,
//                       args // Pass args to constructor
//                   );
//               } else {
//                   designation_chart = new hrms.HierarchyChart(
//                       "Designation",
//                       wrapper,
//                       method,
//                       args // Pass args to constructor
//                   );
//               }

//               frappe.breadcrumbs.add("HR");
//               designation_chart.show();
//           });
//       }).trigger('show'); // Trigger show to refresh the chart
//   }

//   // Initial load without department filter
//   load_chart(wrapper, null);
// };

