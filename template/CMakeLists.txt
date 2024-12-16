add_library( day00 day00.cpp)

target_include_directories(day00 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day00 TBB::tbb )