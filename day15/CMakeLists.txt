add_library( day15 day15.cpp)

target_include_directories(day15 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day15 TBB::tbb )