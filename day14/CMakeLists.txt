add_library( day14 day14.cpp)

target_include_directories(day14 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day14 TBB::tbb )